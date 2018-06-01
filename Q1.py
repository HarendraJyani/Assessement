def validate(s):
    valid = [0,0,0,0]
    if(len(s)>=6 & len(s) <=12):
        for i in range(len(s)):
            if(s[i].isupper()):
                valid[0] = 1
            if(s[i].islower()):
                valid[1] = 1
            if(s[i] in ['#','$','@']):
                valid[2] = 1
        val = 0
        for i in range(len(valid)):
            val = val + valid[i]
        if(val == 3):
            return "Valid Password"
        else:
            return "Invalid Password"

if __name__ == "__main__":
    s = raw_input()
    p = validate(s)
    print(p)
