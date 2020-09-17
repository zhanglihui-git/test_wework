from test_wework.api.department import Department
from test_wework.utils.Utils import Utils


class TestDepartment:
    department = Department()

    def setup_class(self):
        pass

    def test_list(self):
        # list json assert
        # assert depart.list(2).['ddd']=222
        department = Department()
        r = department.list("")
        # print(Utils.format(r))
        assert r["errcode"] == 0
        assert r["department"][0]["name"] == "吉利"

    def test_create(self):
        r = self.department.create("子部门", 1, 1000)
        assert r["errcode"] == 0
        assert r["id"] is not None
        exist = False
        for depart in self.department.list("")["department"]:
            if depart["id"] == r["id"]:
                exist = True

        assert exist == True

    def test_delete(self):
        r = self.department.delete(3)
        assert  r["errcode"] == 0
        exist = True
        for depart in self.department.list("")["department"]:
            if depart["id"] == 3:
                exist == False

        assert  exist == True

