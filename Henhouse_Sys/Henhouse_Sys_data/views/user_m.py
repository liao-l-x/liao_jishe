from Henhouse_Sys_data import models

def branch_company(branch_company_1,branch_company_list):
    #param branch_company_1: 第一层的下属公司列表
    i = 0
    branch = models.company.objects.filter(lead=branch_company_1.id).all()
    if not  branch:
        return  branch_company_1
    else:
        for branch_company_1_noe in branch:
            i = i+1
            branch_company_list.append(branch_company_1_noe)
        return branch_company_list

