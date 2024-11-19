amount = int(input())
no_notes = []
currency = [500,200,100,500,20,10,5,2,1]
for i in currency:
    count = amount//i
    no_notes.append(count)
    print(i,"INR",count,"notes")
    amount = amount%i
print("minimum no.of notes are : ",sum(no_notes))    