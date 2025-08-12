

class employye:

    def __init__(self, name,job_title,salary):

        self.name=name
        self.job_title=job_title
        self.salary=salary

    def show_info(self):
        print(f'name:{self.name},job_title:{self.job_title},salary:{self.salary}')


class manager(employye):
        


 m1=manager('alice','software engineer',2345334335)
 m1.show_info()


    




