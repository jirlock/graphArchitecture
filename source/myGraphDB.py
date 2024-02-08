
#https://graphdb.ontotext.com/documentation/10.5/using-the-graphdb-rest-api.html

import requests
import os
import shutil

importFolderPath = 'C:/Users/jirlo/graphdb-import'

#====================
# importing data
#====================
def copy_rdf_file_to_import_folder(path):
    shutil.copy(path, importFolderPath)
    return None

def delete_rdf_file_from_import_folder(filename):
    os.remove(importFolderPath + '/' + filename)
    return None

def get_server_files(base_url, repo_id):
    url = base_url + '/rest/repositories/' + repo_id + '/import/server'
    return requests.get(url)

def import_server_files(base_url, repo_id, list_of_data_urls):
    url = base_url + '/rest/repositories/' + repo_id + '/import/server'
    data = {
        "fileNames": list_of_data_urls
    }
    return requests.post(url, json=data)

def import_server_files_all(base_url, repo_id):
    url = base_url + '/rest/repositories/' + repo_id + '/import/server'
    res = get_server_files(base_url, repo_id)
    datafile_names = [data["name"] for data in res.json()]
    data = {
        "fileNames": datafile_names
    }
    return requests.post(url, json=data)


#====================
# Repositories
#====================
def get_repositories(base_url):
    return requests.get(base_url + '/rest/repositories')

def get_repository_configuration(base_url, repo_id):
    return requests.get(base_url + '/rest/repositories/' + repo_id)

def get_repository_size(base_url, repo_id):
    return requests.get(base_url + '/rest/repositories/' + repo_id + '/size')

def restart_repository(base_url, repo_id):
    return requests.post(base_url + '/rest/repositories/' + repo_id + '/restart')


#====================
# SPARQL Templates
#====================
def get_sparql_templates(base_url, repo_id):
    return requests.get(base_url + '/rest/repositories/' + repo_id + '/sparql-templates')

def get_sparql_template_configuration(base_url, repo_id, template_id):
    return requests.get(base_url + '/rest/repositories/' + repo_id + 'sparql-templates/configuration', params=template_id)

def create_sparql_template(base_url, repo_id, template_id, query_string):
    url = base_url + '/rest/repositories/' + repo_id + '/sparql-templates'
    data = {
        "query": query_string,
        "templateID": template_id
    }
    return requests.post(url, json=data)

def edit_existing_sparql(base_url, repo_id, template_id, query_string):
    url = base_url + '/rest/repositories/' + repo_id + '/sparql-templates'
    param = {
        "templateID": template_id
    }
    header = {
        "Content-Type": "text/plain"
    }
    return requests.put(url, params=param, headers=header, data=query_string)

def delete_sparql_template(base_url, repo_id, template_id):
    url = base_url + '/rest/repositories/' + repo_id + '/sparql-temlates'
    param = {
        "templateID": template_id
    }
    return requests.delete(url, params=param)

def execute_sparql_template(base_url, repo_id, template_id, json_data):
    url = base_url + '/rest/repositories/' + repo_id + '/sparql-templates/execute'
    json_data["templateId": template_id]
    print(json_data)
    return requests.post(url, json=json_data)


#====================
#Query
#====================
def get_saved_query(base_url, query_name=None):
    url = base_url + '/rest/sparql/saved-queries'
    if query_name:
        param = {
            "name": query_name
        }
        return requests.get(url, params=param)
    else:
        return requests.get(url)

def save_query(base_url, query_name, query_string):
    url = base_url + '/rest/sparql/saved-queries'
    json_data = {
        "body": query_string,
        "name": query_name
    }
    return requests.post(url, json=json_data)

def edit_query(base_url, query_name, query_string):
    url = base_url + '/rest/sparql/saved-queries'
    json_data = {
        "body": query_string,
        "name": query_name
    }
    return requests.put(url, json=json_data)

def delete_query(base_url, query_name):
    url = base_url + '/rest/sparql/saved-queries'
    params = { "name": query_name }
    return requests.delete(url, params=params)

def execute_query(base_url, repo_id, query_name, query_string):
    url = base_url + '/repositories/' + repo_id
    params = {
        "name": query_name,
        "query": query_string
    }
    return requests.get(url, params=params)

def execute_saved_query(base_url, repo_id, query_name):
    url = base_url + '/rest/sparql/saved-queries'
    params = { "name": query_name }
    res = requests.get(url, params=params)
    query_string = res.json()[0]["body"]
    return execute_query(base_url, repo_id, query_name, query_string)

