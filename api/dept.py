import yaml

from api.baseapi import BaseApi
from api.get_token import GetToken
from string import Template


class Dept(BaseApi):
    token = GetToken().get_token()

    # 使用python中的string模板，用来替换yaml文件中的变量，以实现测试步骤的数据驱动
    def Template(self):
        with open("../data/dept.yaml") as f:
            req = Template(f.read()).substitute(access_token=self.token)
            return yaml.safe_load(req)

    def get_dept(self):
        data = self.Template()[0]
        return self.send(data)

    def add_dept(self):
        data = self.Template()[1]
        print(data)
        return self.send(data)

    def update_dept(self):
        data = self.Template()[2]
        return self.send(data)

    def delete_dept(self):
        data = self.Template()[3]
        return self.send(data)

# 调式时使用
# if __name__ == '__main__':
    # get_dept = Dept()
    # get_dept.Template()

    # dept_data = Dept()
    # dept_data.add_dept()