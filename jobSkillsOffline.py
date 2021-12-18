job_skills_map = {
        "data scientist": ['customers', 'Microsoft', "'Advanced", 'customer', 'testing', 'SQL', 'Python', 'business', 'data', 'R'],
        "software engineer": ['software', 'customer', 'degree', 'team', 'communication', 'engineering', 'training', 'integration', 'continuous', 'building'],
        "product manager": ['strategy', 'requirements', 'teams', 'management', 'product', 'define', 'meeting', 'business', 'users', 'development'],
        "software developement engineer": ['development', 'Git', 'software', 'integration', 'engineering', 'C', 'application', 'technical', 'process', 'Agile'],
         "data enginner": ['Devops, Cloud, Python, AWS, SQL, Ansible, relational, pipelines, tableau, Linux'],
         "data analyst": ['AWS', 'business', 'Hadoop', 'statistics', 'solution', 'fintech', 'Hive', 'analytical', 'Github', 'financial'],
        }

def getJobSkills(job):
    return job_skills_map[(job)]

def getAllOfflineJobs():
    return job_skills_map