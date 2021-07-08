from flask import Flask

app = Flask(__name__)
@app.route("/")

def main():

        d1 = int(input("Sides of first dice "))
        d2 = int(input("Sides of second dice "))
        d = []
        dd = []
        out = []
        prob = []

        for i in range (1, (d1+1)):
            d.append(i)

        for i in range (1, (d2+1)):
            dd.append(i)

        for i in range (len(d)):
          for j in range (len(dd)):
            out.append(d[i]+dd[j])

        for i in range (2, (d1 + d2 + 1)):
            x = (out.count(i))/(d1*d2)
            prob.append([i,x])

        print("""
        ------------------
        | Ordered by sum |
        ------------------
        """)

        for i in range (len(prob)):
           print (str(prob[i][0]) + " probability = " + str(prob[i][1]))


        while True:
                Switches = 0
                for i in range(len(prob) - 1):
                    if prob[i][1] > prob[i + 1][1]:
                        x = prob[i + 1]
                        prob[i + 1] = prob[i]
                        prob[i] = x
                        Switches += 1
                    else:
                        pass
                if Switches == 0:
                    break

        print("""
        --------------------------
        | Ordered by probability |
        --------------------------
        """) 

        for i in range (len(prob)):
           print (str(prob[i][0]) + " probability = " + str(prob[i][1]))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
