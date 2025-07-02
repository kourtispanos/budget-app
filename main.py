# MyBudgetApp - Έξυπνος υπολογισμός προϋπολογισμού

def calculate_budget():
    print("💰 Καλωσήρθες στο MyBudgetApp!\n")

    try:
        income = float(input("🔹 Πόσα είναι τα έσοδά σου (€); "))
        expenses = float(input("🔻 Πόσα είναι τα έξοδά σου (€); "))
    except ValueError:
        print("❌ Παρακαλώ εισάγετε έγκυρους αριθμούς.")
        return

    leftover = income - expenses

    print("\n📊 Αποτελέσματα:")
    print(f"➡️ Καθαρό υπόλοιπο: {leftover:.2f} €")

    if leftover > 0:
        savings = leftover * 0.20
        print(f"💡 Πρόταση: Βάλε στην άκρη τουλάχιστον {savings:.2f} € για αποταμίευση.")
    elif leftover == 0:
        print("⚠️ Δεν σου μένει τίποτα. Ίσως χρειάζεσαι καλύτερη διαχείριση.")
    else:
        print("❗ Ξοδεύεις περισσότερα απ' ό,τι βγάζεις. Προσοχή!")

if __name__ == "__main__":
    calculate_budget()
