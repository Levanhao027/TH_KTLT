print("SV: Le Van Hao")
print("MSSV: 235752021610027")
def calculate_balance (transactions):
    balance = 0
    # Initialize account balance
   for transaction in transactions:
      action, amount = transaction.split()
      # Separate action and amount
      amount int (amount)
      # Convert amount to integer type
      if action == 'D':
          # Deposits
          balance += amount
      elif action == 'W':
          # Withdrawal
          balance -= amount
  return balance
# Import transaction logs from users
input_transactions = []
print("Enter transaction log (enter 'x' to finish): ")
while True:
    transaction = input()
    if transaction.lower() == 'x':
        # Ends when user enters 'x'
        break
    input_transactions.append(transaction)
# Calculate the actual amount in the account
final_balance = calculate_balance (input_transactions)
# Print the results
print("actual amount in account is:", final_balance)
