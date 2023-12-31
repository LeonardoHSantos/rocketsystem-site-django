import json
import requests
from config_app import API_TOKEN, COMPANY_DOMAIN, CUSTOM_FIELDS_PIPEDRIVE

class API_Pipedrive:
    def __init__(self, api_token, company_domain):
        self.api_token = api_token
        self.company_domain = company_domain
    # ---
    def get_person(self, person_id):
        print(f">>> person_id: {person_id}")

        try:
            url = f"https://{self.company_domain}.pipedrive.com/api/v1/persons/{person_id}?api_token={self.api_token}"
            response = requests.get(url)
            result = response.json()
            # print("\n\n\n------------------> PERSON DATA")
            # print(result)

            if not result["success"]:
                return {"code": 401, "msg": "person - falha ao obter dados."}
            # ---
            elif result["data"]["id"]:
                result = result["data"]
                # print("\n\n\n\n\n------------------------------->>> DATA")
                # print(result)
                data = {
                    "id": {"field_edit": False, "type": "text", "value": person_id},
                    "name": {"field_edit": True, "type": "text", "value": result["name"]},
                    "phone": {"field_edit": True, "field_object": True, "type": "text", "value": result["phone"]},
                    "email": {"field_edit": True, "field_object": True, "type": "email", "value": result["email"]},
                    "cpf": {"field_edit": False, "type": "text", "value": result[CUSTOM_FIELDS_PIPEDRIVE["cpf"]]},
                    "cnpj": {"field_edit": False, "type": "text", "value": result[CUSTOM_FIELDS_PIPEDRIVE["cnpj"]]},
                }
                data_resume = {
                    "id": {"field_edit": False, "type": "text", "value": person_id},
                    "org_name": {"field_edit": False, "type": "text", "value": result["org_name"]},
                    "company_id": {"field_edit": False, "type": "text", "value": result["company_id"]},
                    "owner": {"field_edit": False, "type": "text", "value": result["owner_id"]["name"]},
                    "open_deals_count": {"field_edit": False, "type": "text", "value": result["open_deals_count"]},
                    "closed_deals_count": {"field_edit": False, "type": "text", "value": result["closed_deals_count"]},
                    "add_time": {"field_edit": False, "type": "text", "value": result["add_time"]},
                    "update_time": {"field_edit": False, "type": "text", "value": result["update_time"]},
                    "cpf": {"field_edit": False, "type": "text", "value": result[CUSTOM_FIELDS_PIPEDRIVE["cpf"]]},
                    "cnpj": {"field_edit": False, "type": "text", "value": result[CUSTOM_FIELDS_PIPEDRIVE["cnpj"]]},
                }
                # print("******************************* RESUME")
                # print(data_resume)
                return {
                    "code": 200,
                    "data": data,
                    "data_resume": data_resume,
                }
        except Exception as e:
            print(f"\n ### ERRO AO OBTER DADOS PERSON | ERRO: {e}")
            return {"code": 500, "msg": "person - houve algum erro com o servidor."}
    # ---
    def update_person(self, person_id, data):
        # print(data)
        try:

            url = f"https://{COMPANY_DOMAIN}.pipedrive.com/api/v1/persons/{person_id}?api_token={API_TOKEN}"
            headers = {'content-type': 'application/json'}
            response = requests.put(
                url=url,
                headers=headers,
                data= json.dumps(data),
                )
            result = response.json()
            if not result["success"]:
                print("\n\n\n>>>", result)
                return {"code": 401, "msg": "person - falha ao atualizar dados."}

            elif result["data"]["id"]:
                return {
                    "code": 200,
                    "msg": "person - dados atualizados com sucesso."
                }
        except Exception as e:
            print(f"\n ### ERRO AO ATUALIZAR PERSON | ERRO: {e}")
            return {"code": 500, "msg": "person - houve algum erro com o servidor."}
    # ---
    def create_person(self, data):
        # print(data)
        try:

            url = f"https://{COMPANY_DOMAIN}.pipedrive.com/api/v1/persons?api_token={API_TOKEN}"
            headers = {'content-type': 'application/json'}
            response = requests.post(
                url=url,
                headers=headers,
                data= json.dumps(data),
                )
            result = response.json()
            if not result["success"]:
                print("\n\n\n>>>", result)
                return {"code": 401, "msg": "falha ao criar person."}

            elif result["data"]["id"]:
                return {
                    "code": 200,
                    "msg": "person adicionado com sucesso."
                }
        except Exception as e:
            print(f"\n ### ERRO AO CRIAR PERSON | ERRO: {e}")
            return {"code": 500, "msg": "person - houve algum erro com o servidor."}
    
    # ---
    def delete_person(self, id_person):
        # print(data)
        try:
            url = f"https://{COMPANY_DOMAIN}.pipedrive.com/api/v1/persons/{id_person}/?api_token={API_TOKEN}"
            headers = {'content-type': 'application/json'}
            response = requests.delete(
                url=url,
                headers=headers
            )
            result = response.json()
            if not result["success"]:
                print("\n\n\n>>>", result)
                return {"code": 401, "msg": "falha ao deletar pessoa."}

            elif result["data"]["id"]:
                return {
                    "code": 200,
                    "msg": "person deletada com sucesso."
                }
        except Exception as e:
            print(f"\n ### ERRO AO DELETAR PERSON | ERRO: {e}")
            return {"code": 500, "msg": "person - houve algum erro com o servidor."}
    # ---
    def get_fields(self):
        url = f'https://{self.company_domain}.pipedrive.com/api/v1/personFields:(key,name)?start=0&api_token={self.api_token}'
        # print(f"\n\n **** URL PERSON FIELDS: {url}")
        response = requests.get(url)
        # print(response)
        if not response.json()['data']:
            exit(f"Error: {response.json()['error']}")
        
        fieldsObject = {
            "cpf": None,
            "cnpj": None,
            "service_name_contact": None
        }
        for field in response.json()['data']:
            if field["name"] == "cpf":
                fieldsObject["cpf"] = field["key"]
                # print(f"------- DATA: {field}")
            if field["name"] == "cnpj":
                fieldsObject["cnpj"] = field["key"]
                # print(f"------- DATA: {field}")
            if field["name"] == "service_name_contact":
                fieldsObject["service_name_contact"] = field["key"]
                # print(f"------- DATA: {field}")
        return fieldsObject




if __name__ == "__main__":
    API = API_Pipedrive(api_token=API_TOKEN, company_domain=COMPANY_DOMAIN)
    
    data = {
        "org_id": 3,
        "label": 8,
        "name": "Leonardo - Teste API - 4",
        "phone": [
            {
                "label": "work",
                "value": "(41) 9 8841-2653",
                "primary": True
            },
            {
                "label": "work",
                "value": "(41) 9 1111-1111",
                "primary": False
            }
        ],
        "email": [
            {
                "label": "work",
                "value": "ti@demandareal.com",
                "primary": True
            },
            {
                "label": "work",
                "value": "ti@socketsystem.tech",
                "primary": False
            }
        ]
    }
    # update_P = API.update_person(person_id=1, data=data)
    # print(update_P)
    # ---
    get_person = API.get_person(person_id=1)
    print(get_person)
    data = get_person["msg"]["data"]
    for key, value in data.items():
        print(f"key: {key} | valor: {value}")