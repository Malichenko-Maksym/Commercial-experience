
class Ministry_of_Health:
    number_of_workers = 690
    year_budget_mln = 350
    current_leader = "Viktor Liashko"
    main_office_address = "Hrushewskogo 7"

    def change_leader(self, new_leader):
        self.current_leader = new_leader

    def increase_the_budget(self, additional_cash_mln):
        self.year_budget_mln = additional_cash_mln + self.year_budget_mln

    def hire_a_worker(self):
        self.number_of_workers= self.number_of_workers + 1

cash=int(input("How much money you need? "))
Ukrainian_health = Ministry_of_Health()
Ukrainian_health.increase_the_budget(cash)
print("Information about Ukraine")
print(Ukrainian_health.year_budget_mln)
print(Ukrainian_health.current_leader)
print("\n")

USA_health = Ministry_of_Health()
USA_health.change_leader("John Montana")
print("Information about USA")
print(USA_health.year_budget_mln)
print(USA_health.current_leader)
