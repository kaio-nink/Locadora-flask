import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.Scanner;

import javax.xml.transform.Result;

public class App {
    public static void main(String[] args) throws Exception {
        final String URL = "jdbc:mysql://localhost/mercado";
        final String USER = "harison";
        final String PASSWORD = "12345";
        Connection con = null;
        try {
            con = DriverManager.getConnection(URL, USER, PASSWORD);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
            System.exit(1);
        }

        System.out.println("Conexão com BD_Mercado estabelecida");

        int opcao = 0;
        Scanner leitor = new Scanner(System.in);

        while (true) {
            System.out.println("\n********* MENU *********");
            System.out.println("(1) Cadastrar cliente\n(2) Cadastrar produto\n(3) Lançar venda\n(4) sair");
            System.out.println("************************");

            opcao = leitor.nextInt();
            leitor.nextLine();
            if (opcao == 4) {
                try{
                    con.close();
                    System.out.println("CONEXÃO ENCERRADA !!");
                    leitor.close();
                }catch(SQLException e){
                    System.out.println(e.getMessage());
                }
            }
            switch (opcao) {
                case 1:
                    System.out.print("Id: ");
                    int id_cliente = leitor.nextInt();
                    leitor.nextLine();

                    System.out.print("Nome: ");
                    String nome = leitor.nextLine();

                    System.out.print("CPF: ");
                    String cpf = leitor.nextLine();
                    //leitor.nextLine();

                    boolean ret1 = cadastrarCliente(con, id_cliente, nome, cpf);
                    if (ret1) {
                        System.out.println("Cliente cadastrado!");
                    } else {
                        System.out.println("Não foi possível cadastrar o/a cliente");
                    }

                    break;
                    
                case 2:
                    System.out.print("Id: ");
                    int id_prod = leitor.nextInt();
                    leitor.nextLine();

                    System.out.print("Nome: ");
                    String nome_prod = leitor.nextLine();

                    System.out.print("Preco unitário: ");
                    float preco_unit = leitor.nextFloat();
                    leitor.nextLine();

                    System.out.print("Quantidade: ");
                    int qtd = leitor.nextInt();
                    leitor.nextLine();

                    boolean ret2 = cadastrarProduto(con, id_prod, nome_prod, preco_unit, qtd);
                    if (ret2) {
                        System.out.println("Produto cadastrado!");
                    } else {
                        System.out.println("Não foi possível cadastrar o produto");
                    }
                    break;
                case 3:
                    System.out.println("Entre com o primeiro nome o cliente");
                    nome = leitor.nextLine();
                    ResultSet rsCliente = getClientes(con, nome);
                    System.out.println("*********** Clientes cadastrados **************");
                    if(rsCliente != null){
                        while(rsCliente.next()){
                            System.out.println("ID = "+rsCliente.getInt(1)+" Nome = "+rsCliente.getString(2));
                        }
                    }else{
                        break;
                    }
                    System.out.println("************* Produtos cadastrados **************");
                    if(getProduto(con) == false){
                        break;
                    }

                    // Efetuar vendas
                    System.out.println("Entre com o id do cliente: ");
                    id_cliente = leitor.nextInt();
                    leitor.nextLine(); // LIMPAR BUFFER
                    System.out.println("Entre com o id do produto: ");
                    id_prod = leitor.nextInt();
                    leitor.nextLine();
                    System.out.println("Entre com o id da compra: ");
                    int id = leitor.nextInt();
                    leitor.nextLine();
                    LocalDate data = LocalDate.now(); //data de hoje
                    System.out.println("Entre com a quatidade: ");
                    int qtdVendida = leitor.nextInt();
                    leitor.nextLine();

                    cadastrarVenda(con, id_cliente, id_prod, id, data, qtdVendida);

                    break;
                default:
                    System.out.println("Opção inválida!");
                    break;
            }
            
        }
    }

    public static boolean cadastrarCliente(Connection con, int id_cliente, String nome, String cpf) {
        final String sql = "INSERT INTO cliente VALUES(?,?,?)";

        try {
            PreparedStatement stm = con.prepareStatement(sql);
            stm.setInt(1, id_cliente);
            stm.setString(2, nome);
            stm.setString(3, cpf);
            stm.executeUpdate();
            return true;

        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }

    }

    public static boolean cadastrarProduto(Connection con, int id_produto, String nome, float preco_unitario, int qtd) {
        final String sql = "INSERT INTO produto VALUES(?,?,?,?)";

        try {
            PreparedStatement stm = con.prepareStatement(sql);
            stm.setInt(1, id_produto);
            stm.setString(2, nome);
            stm.setFloat(3, preco_unitario);
            stm.setInt(4, qtd);
            stm.executeUpdate();
            return true;

        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }

    }
    
    public static ResultSet getClientes(Connection con, String nome){
        String sql = "select id_cliente, nome from cliente where nome like ?";
        
        try{
            PreparedStatement stm = con.prepareStatement(sql);
            stm.setString(1, nome+"%");
            ResultSet rs = stm.executeQuery();
            return rs;
            
        }catch(SQLException e){
            System.out.println(e.getMessage());
            return null;
        }
    }

    public static boolean getProduto(Connection con){
        String sql = "select * from produto";

        try{
            PreparedStatement stm = con.prepareStatement(sql);
            ResultSet rs = stm.executeQuery();
            while(rs.next()){
                System.out.println("ID: "+ rs.getInt(1)+ "NOME: "+ rs.getString(2) + "PREÇO: "+ 
                    rs.getFloat(3) + "QTD:" + rs.getInt(4));
            }
            return true;
        }catch(SQLException e){
            System.out.println(e.getMessage());
            return false;
        }
    }

    public static boolean cadastrarVenda(Connection con, int id_cliente, int id_produto, int id, LocalDate data, int qtdVendida){
        String sql = "update produto set qtd = qtd - ? where id_produto = ?";

        try{
            PreparedStatement stm = con.prepareStatement(sql);
            stm.setInt(1, qtdVendida);
            stm.setInt(2, id_produto);
            stm.executeUpdate();
            
        }catch(SQLException e){
            System.out.println(e.getMessage());
            return false;
        }

        // registrar a venda

        sql = "insert into compras values(?,?,?,?,?)";

        try{
            PreparedStatement stm = con.prepareStatement(sql);
            stm.setInt(1, id);
            stm.setInt(2, id_cliente);
            stm.setInt(3, id_produto);
            stm.setDate(4, Date.valueOf(data));
            stm.setInt(5, qtdVendida);
            stm.executeUpdate();
            return true;
        }catch(SQLException e){
            System.out.println(e.getMessage());
            return false;
        }
    }
}