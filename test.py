import re

sql_query = """
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
    AND o.type_contrat IN ('CDI', 'CDD');
"""

