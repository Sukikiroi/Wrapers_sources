# IDs wraper
# from api_wraper import api_wraper
from csv_wraper import csv_wraper
from helpers import check_columns_in_csv, extract_columns_from_sql

csv_file_path = "C:\\Users\\rabeh\\Desktop\\TP Ala\\codeing\\minioffre.csv"
# Views
view_01 = """CREATE VIEW job_offre_filtered AS
SELECT 
    o.id,
    o.titre,
    o.entreprise,
    o.ville,
    o.type_contrat,
    o.salaire_min * 1.15 AS salaire_min_adjusted,
    o.salaire_max,
    o.date_publication,
    o.description
FROM job_offre o
WHERE o.salaire_max IS NOT NULL
AND o.salaire_min IS NOT NULL
AND o.type_contrat IN ('CDI', 'CDD'); """


# Decision


#  extract les columns from source and make decision  to choose between wrapers


def decision(view):
    list_wraper=[]
    # return name of wraper
    columns = extract_columns_from_sql(view)

    # if columns Exist in source select it
    if  check_columns_in_csv(csv_file_path, columns):
        list_wraper.append("csv_wraper")
    
    return list_wraper


 
def manage_wrapers_():
    list_activated_wraper = decision(view_01)
     

    for wraper in list_activated_wraper:


        if wraper == "csv_wraper":
            csv_wraper()

      # if wraper == "api_wraper":
        #     api_wraper()


manage_wrapers_()


