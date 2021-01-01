def what(a,b):
    if a>b:
        print("Decrescente")
    elif a<b:
        print("Crescente")
a,b = input().split();
what(int(a),int(b));
