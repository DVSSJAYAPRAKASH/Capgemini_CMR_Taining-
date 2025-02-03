class orders:
    def __init__(self):
        self.ordersid = int(input("Enter Order ID: "))
        self.orderstatus = input("Enter Order Status: ")
        self.orderdate = input("Enter Order Date: ")
        self.requireddate = input("Enter Required Date: ")
        self.shipdate = input("Enter Ship Date: ")
        self.storeid = int(input("Enter Store ID: "))
        self.staffid = int(input("Enter Staff ID: "))