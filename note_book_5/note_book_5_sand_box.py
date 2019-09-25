def is_ssn(s):
    parts=s.split('-')
    correct_length=[3,2,4]
    for p,n in zip(parts,correct_length):
        if (p.isdigit() and len(p)==n):
            return True
        else:
            return False



