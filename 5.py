import numpy as np

def fibo ( kolom , baris  ) :
    jumlah_cell = kolom * baris
    barisan_fibo = np.zeros ( jumlah_cell ).astype(int)
    cell_ke = 0
    for i  in range ( baris ) :
        for j in range ( kolom ) :
            if ( cell_ke == 0 ) :
                barisan_fibo [ cell_ke ] = 0
            elif ( cell_ke == 1 ) :
                barisan_fibo [ cell_ke ] = 1
            else:
                barisan_fibo [ cell_ke ] = barisan_fibo [ cell_ke - 1 ] + barisan_fibo [ cell_ke - 2 ]
            
            print (barisan_fibo [ cell_ke ] , ', ' , sep='' , end = '')
            cell_ke = cell_ke + 1
        print('')