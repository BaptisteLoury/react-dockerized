import jwt

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZXhwIjoxNjc2Mjc4Mjg2fQ.Zg3krtiiKrTBHocA6rHPC6PsNLDD2Ktjk2gN9uqufiw"

print(jwt.decode(token, "heyheyhey", algorithms='HS256'))