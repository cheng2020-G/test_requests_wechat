import yaml

from api.baseapi import BaseApi
from api.get_token import GetToken
from string import Template


class Dept(BaseApi):
    token = GetToken().get_token()

    # 使用python中的string模板，用来替换yaml文件中的变量，以实现测试步骤的数据驱动
    def Template(self):
        with open("../data/get_dept.yaml") as f:
            req = Template(f.read()).substitute(access_token=self.token)
            print(req)
            return yaml.safe_load(req)

    def get_dept(self):
        data = self.Template()
        return self.send(data)

    def add_dept(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create?",
            "params": {
                "access_token": self.token,
                "name": "北京部门",
                "name_en": "dept-bj",
                "parentid": 1,
                "order": 1,
                "id": 10
            }
        }
        return self.send(data)

    def update_dept(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/update?",
            "params": {
                "access_token": self.token,
                "id": 5,
                "name": "爱测测试平台",
                "name_en": "ceshier",
                "parentid": 1,
                "order": 1
            }
        }
        return self.send(data)

    def delete_dept(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/delete?",
            "params": {
                "access_token": self.token,
                "id": 4
            }
        }
        return self.send(data)

# 调式时使用
# if __name__ == '__main__':
#     get_dept = Dept()
#     get_dept.Template()
