create function media_ponderada(x int, y int, z int, w int) returns int
    begin 
        declare m int;
        set m = (x + 2*y + 3*z + 4*w)/10;
        return m;
    end$$