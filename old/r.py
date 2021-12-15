    #     i1,i2 = [i for i in range(n_times) if schedule[i][r] == t1 or schedule[i][r] == t2]
    #     r1 = schedule[i1][r]
    #     r2 = schedule[i2][r]
    # for i in range(n_times):
    #     if i == t1 or i == t2:
    #         continue
    #     r1 = schedule[i].index(t1)
    #     r2 = schedule[i].index(t2)
    #     if r1 > r2:
    #         r1,r2 = r2,r1
    #         t1,t2 = t2,t1
    #         if r1 == 0 and r2==n_times-2:
    #             td1 = schedule[i][r1+1]
    #             te2 = schedule[i][r2-1]

    #             new_obj -= (
    #                 (weight_table[t2][t1] * aux_carry_over_table[t2][t1]**2) + 
    #                 (weight_table[t1][td1] * aux_carry_over_table[t1][td1]**2) + 
    #                 (weight_table[te2][t2] * aux_carry_over_table[te2][t2]**2) +

    #                 (weight_table[t1][t2] * aux_carry_over_table[t1][t2]**2) +
    #                 (weight_table[t2][td1] * aux_carry_over_table[t2][td1]**2) +
    #                 (weight_table[te2][t1] * aux_carry_over_table[te2][t1]**2)
    #             )

    #             aux_carry_over_table[t2][t1] -=1
    #             aux_carry_over_table[t1][td1] -=1
    #             aux_carry_over_table[te2][t2] -=1
    #             aux_carry_over_table[t1][t2] +=1
    #             aux_carry_over_table[t2][td1] +=1
    #             aux_carry_over_table[te2][t1] +=1

    #             new_obj += (
    #                 (weight_table[t2][t1] * aux_carry_over_table[t2][t1]**2) + 
    #                 (weight_table[t1][td1] * aux_carry_over_table[t1][td1]**2) + 
    #                 (weight_table[te2][t2] * aux_carry_over_table[te2][t2]**2) +

    #                 (weight_table[t1][t2] * aux_carry_over_table[t1][t2]**2) +
    #                 (weight_table[t2][td1] * aux_carry_over_table[t2][td1]**2) +
    #                 (weight_table[te2][t1] * aux_carry_over_table[te2][t1]**2)
    #             )
    #         elif r2-r1 == 1:
            
    #             t1 = schedule[i][r1]
    #             t2 = schedule[i][r2]

    #             if r1 != 0:
    #                 te1 = schedule[i][r1-1]
    #             else:
    #                 te1 = schedule[i][n_times-2]
    #             if r2 != n_times-2:
    #                 td2 = schedule[i][r2+1]
    #             else:
    #                 td2 = schedule[i][0]
                
    #             new_obj -= (
    #                 (weight_table[t1][t2] * aux_carry_over_table[t1][t2]**2) + 
    #                 (weight_table[te1][t1] * aux_carry_over_table[te1][t1]**2) + 
    #                 (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +

    #                 (weight_table[t2][t1] * aux_carry_over_table[t2][t1]**2) +
    #                 (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2) +
    #                 (weight_table[te1][t2] * aux_carry_over_table[te1][t2]**2)
    #             )

    #             aux_carry_over_table[t1][t2] -=1
    #             aux_carry_over_table[te1][t1] -=1
    #             aux_carry_over_table[t2][td2] -=1
    #             aux_carry_over_table[t2][t1] +=1
    #             aux_carry_over_table[t1][td2] +=1
    #             aux_carry_over_table[te1][t2] +=1

    #             new_obj += (
    #                 (weight_table[t1][t2] * aux_carry_over_table[t1][t2]**2) + 
    #                 (weight_table[te1][t1] * aux_carry_over_table[te1][t1]**2) + 
    #                 (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +

    #                 (weight_table[t2][t1] * aux_carry_over_table[t2][t1]**2) +
    #                 (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2) +
    #                 (weight_table[te1][t2] * aux_carry_over_table[te1][t2]**2)
    #             )
    #         elif r2-r1 == 2:
    #             t1 = schedule[i][r1]
    #             t2 = schedule[i][r2]

    #             if r1 != 0:
    #                 te1 = schedule[i][r1-1]
    #             else:
    #                 te1 = schedule[i][n_times-2]

    #             td1 = schedule[i][r1+1]

    #             if r2 != n_times-2:
    #                 td2 = schedule[i][r2+1]
    #             else:
    #                 td2 = schedule[i][0]

    #             new_obj -= (
    #                 (weight_table[te1][t1] * aux_carry_over_table[te1][t1]**2) + 
    #                 (weight_table[t1][td1] * aux_carry_over_table[t1][td1]**2) + 
    #                 (weight_table[td1][t2] * aux_carry_over_table[td1][t2]**2) +
    #                 (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +

    #                 (weight_table[td1][t1] * aux_carry_over_table[td1][t1]**2) +
    #                 (weight_table[te1][t2] * aux_carry_over_table[te1][t2]**2)+
    #                 (weight_table[t2][td1] * aux_carry_over_table[t2][td1]**2)+
    #                 (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2)
    #             )

    #             aux_carry_over_table[te1][t1] -=1
    #             aux_carry_over_table[t1][td1] -=1
    #             aux_carry_over_table[td1][t2] -=1
    #             aux_carry_over_table[t2][td2] -=1

    #             aux_carry_over_table[td1][t1] +=1
    #             aux_carry_over_table[te1][t2] +=1
    #             aux_carry_over_table[t2][td1] +=1
    #             aux_carry_over_table[t1][td2] +=1

    #             new_obj += (
    #                 (weight_table[te1][t1] * aux_carry_over_table[te1][t1]**2) + 
    #                 (weight_table[t1][td1] * aux_carry_over_table[t1][td1]**2) + 
    #                 (weight_table[td1][t2] * aux_carry_over_table[td1][t2]**2) +
    #                 (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +

    #                 (weight_table[td1][t1] * aux_carry_over_table[td1][t1]**2) +
    #                 (weight_table[te1][t2] * aux_carry_over_table[te1][t2]**2)+
    #                 (weight_table[t2][td1] * aux_carry_over_table[t2][td1]**2)+
    #                 (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2)
    #             )

    #         elif r2-r1 >= 3:
    #             t1 = schedule[i][r1]
    #             t2 = schedule[i][r2]

    #             td1 = schedule[i][r1+1]
    #             te2 = schedule[i][r2-1]

    #             if r1 != 0:
    #                 te1 = schedule[i][r1-1]
    #             else:
    #                 te1 = schedule[i][n_times-2]
    #             if r2 != n_times-2:
    #                 td2 = schedule[i][r2+1]
    #             else:
    #                 td2 = schedule[i][0]

    #             new_obj -= (
    #                 (weight_table[te1][t1] * aux_carry_over_table[te1][t1]**2) + 
    #                 (weight_table[t1][td1] * aux_carry_over_table[t1][td1]**2) + 
    #                 (weight_table[te2][t2] * aux_carry_over_table[te2][t2]**2) +
    #                 (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +

    #                 (weight_table[te1][t2] * aux_carry_over_table[te1][t2]**2) +
    #                 (weight_table[t2][td1] * aux_carry_over_table[t2][td1]**2)+
    #                 (weight_table[te2][t1] * aux_carry_over_table[te2][t1]**2)+
    #                 (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2)
    #             )

    #             aux_carry_over_table[te1][t1] -=1
    #             aux_carry_over_table[t1][td1] -=1
    #             aux_carry_over_table[te2][t2] -=1
    #             aux_carry_over_table[t2][td2] -=1

    #             aux_carry_over_table[te1][t2] +=1
    #             aux_carry_over_table[t2][td1] +=1
    #             aux_carry_over_table[te2][t1] +=1
    #             aux_carry_over_table[t1][td2] +=1

    #             new_obj += (
    #                 (weight_table[te1][t1] * aux_carry_over_table[te1][t1]**2) + 
    #                 (weight_table[t1][td1] * aux_carry_over_table[t1][td1]**2) + 
    #                 (weight_table[te2][t2] * aux_carry_over_table[te2][t2]**2) +
    #                 (weight_table[t2][td2] * aux_carry_over_table[t2][td2]**2) +

    #                 (weight_table[te1][t2] * aux_carry_over_table[te1][t2]**2) +
    #                 (weight_table[t2][td1] * aux_carry_over_table[t2][td1]**2)+
    #                 (weight_table[te2][t1] * aux_carry_over_table[te2][t1]**2)+
    #                 (weight_table[t1][td2] * aux_carry_over_table[t1][td2]**2)
    #             )
        #print(f'r:{r} i5:{i5} i6:{i6} t5:{t5} t6:{t6}')

        # if r == 0:

        #     t5e = schedule[i5][-1]
        #     t6e = schedule[i6][-1]
        # else:
            
        #     t5e = schedule[i5][r-1]
        #     t6e = schedule[i6][r-1]

        # if r == n_times-2:
            
        #     t5d = schedule[i5][0]
        #     t6d = schedule[i6][0]  

        # else:
            
        #     t5d = schedule[i5][r+1]
        #     t6d = schedule[i6][r+1]    
        
        # print(t5e,t5,t5d,' ',t6e,t6,t6d)

        # new_obj -= (

        #     (weight_table[t5e][t5] * aux_carry_over_table[t5e][t5]**2) + 
        #     (weight_table[t5][t5d] * aux_carry_over_table[t5][t5d]**2) + 
        #     (weight_table[t6e][t6] * aux_carry_over_table[t6e][t6]**2) +
        #     (weight_table[t6][t6d] * aux_carry_over_table[t6][t6d]**2) +

        #     (weight_table[t5e][t6] * aux_carry_over_table[t5e][t6]**2) + 
        #     (weight_table[t6][t5d] * aux_carry_over_table[t6][t5d]**2) + 
        #     (weight_table[t6e][t5] * aux_carry_over_table[t6e][t5]**2) +
        #     (weight_table[t5][t6d] * aux_carry_over_table[t5][t6d]**2) 
        # )

        # aux_carry_over_table[t5e][t5] -=1
        # aux_carry_over_table[t5][t5d] -=1
        # aux_carry_over_table[t6e][t6] -=1
        # aux_carry_over_table[t6][t6d] -=1

        # aux_carry_over_table[t5e][t6] +=1
        # aux_carry_over_table[t6][t5d] +=1
        # aux_carry_over_table[t6e][t5] +=1
        # aux_carry_over_table[t5][t6d] +=1

        # new_obj += (

        #     (weight_table[t5e][t5] * aux_carry_over_table[t5e][t5]**2) + 
        #     (weight_table[t5][t5d] * aux_carry_over_table[t5][t5d]**2) + 
        #     (weight_table[t6e][t6] * aux_carry_over_table[t6e][t6]**2) +
        #     (weight_table[t6][t6d] * aux_carry_over_table[t6][t6d]**2) +

        #     (weight_table[t5e][t6] * aux_carry_over_table[t5e][t6]**2) + 
        #     (weight_table[t6][t5d] * aux_carry_over_table[t6][t5d]**2) + 
        #     (weight_table[t6e][t5] * aux_carry_over_table[t6e][t5]**2) +
        #     (weight_table[t5][t6d] * aux_carry_over_table[t5][t6d]**2) 
        # )