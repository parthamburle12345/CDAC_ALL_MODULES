from abc import ABC,abstractmethod

class Account(ABC):
    @abstractmethod
    def do_job(self):
        pass

def Business(acc_lst):
    print("Business Started")
    for acc in acc_lst:
        acc.do_job()
    else:
        print("Completed All account type verification")
    print("Business Completed")
print("_" * 60)
# -----------------------------------------------------

class Savings(Account):
    def do_job(self):
        print("Savings job done")

class Current(Account):
    def do_job(self):
        print("Current job done")

class DMat(Account):
    def do_job(self):
        print("DMat job done")

class OD(Account):
    def do_job(self):
        print("OD job done")

# acc = Account() # Can't instantiate abstract class Account

# sa = Savings()
# curr =  Current()
# dmat = DMat()

# Business([sa,curr,dmat])
# sub_classes = [sub for sub in Account.__subclasses__()]
sub_classes = [sub.__name__ for sub in Account.__subclasses__()]
print(sub_classes)
str_class_name = "Savings"
# sub_object =[ eval(f"{str_class_name}()")]
sub_object = [eval(f"{sub.__name__}()") for sub in Account.__subclasses__()]
Business(sub_object)
