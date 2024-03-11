
#transactions year 2020
#initial=0
#transactions(amount,date)
#amount less than 0 that is negative=card payment else incoming transfer
#yyyy-mm-dd
#card fee 5 per month-omitted in the transaction list
#fee deducted from the account balance at the end of each month unless there were at least three payments made by card for a total cost of at least 100 within a month.
#required =final balance of the account at the end of the year 2020
#def solution(A,D)
#array A of N integers rep transcaction amounts 
#array D of N  strings represnts transaction dates 
#should return final balance of the account
#transaction number K (for Kwithin the range [0... N-1]) was represented by D[K] for amount A[k]Y
#function solution(A) {
    #let currentNode = 0; // Start from the head of the list
   # let length = 0; // Initialize the length of the list

  #  while (A[currentNode] !== -1) {
   #     currentNode = A[currentNode]; // Move to the next node
   #     length++; // Increment the length of the list
    #}

   # // Add 1 for the last node with value -1
   # return length + 1;
#}

#// Example usage:
#const A = [1, 4, -1, 3, 2];
#console.log(solution(A)); // Output should be 3


def solution(A,D):
    # Initialize the final balance to 0
    final_balance = 0
    
    # Iterate through each transaction
    for i in range(len(A)):
        if D[i] == "2020-01-01":
            # If the transaction is the first transaction of the year
            final_balance = A[i]
        elif D[i] == "2020-12-31":
            # If the transaction is the last transaction
            break
        else:
            # Otherwise, add the transaction amount to the  final balance
            final_balance += A[i]

          

        # If the transaction is a card payment
        if A[i] < 0:
            # Deduct the card fee from the final balance
            final_balance -= 5
        else:
            # Add the incoming transfer to the final balance
            final_balance += A[i]
    
    print (final_balance)

# Testing the function with example inputs
A = [-60, 60, -40, -20]
D= ["2020-10-01", "2020-02-02", "2020-10-10", "2020-10-30"]
solution(A,D)




