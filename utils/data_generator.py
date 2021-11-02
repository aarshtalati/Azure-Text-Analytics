import random

f_name: str = "../data/input"
f_ext: str = "csv"

# fake data generators:
#   https://generatedata.com/
#   https://theonegenerator.com/

people = [
    {
        "name": "Chase Keith",
        "phone": "1-698-676-8447",
        "email": "lorem.eu.metus@vestibulumante.co.uk",
        "currency": "471617 1842683256",
        "SSN": "387746078"
    },
    {
        "name": "Declan Craig",
        "phone": "1-664-254-0925",
        "email": "senectus.et@dolornullasemper.ca",
        "currency": "649338 522188 8844",
        "SSN": "577-92-4085"
    },
    {
        "name": "Brynn Wood",
        "phone": "1-532-228-5545",
        "email": "parturient@ac.co.uk",
        "currency": "362533261856681",
        "SSN": "525-32-5026"
    },
    {
        "name": "Jessica Sawyer",
        "phone": "(547) 269-4650",
        "email": "dui@ipsumdolor.co.uk",
        "currency": "5227287261647754",
        "SSN": "318428501"
    },
    {
        "name": "Deborah Wilder",
        "phone": "(396) 526-5598",
        "email": "sodales.elit.erat@sed.com",
        "currency": "538 86185 49867 555",
        "SSN": "237-73-0391"
    },
    {
        "name": "Chase Keith",
        "phone": "1-698-676-8447",
        "email": "lorem.eu.metus@vestibulumante.co.uk",
        "currency": "646 43352 87273 410",
        "SSN": "050469196"
    },
    {
        "name": "Declan Craig",
        "phone": "1-664-254-0925",
        "email": "senectus.et@dolornullasemper.ca",
        "currency": "633469 547132 3588",
        "SSN": "440-34-6703"
    },
    {
        "name": "Brynn Wood",
        "phone": "1-532-228-5545",
        "email": "parturient@ac.co.uk",
        "currency": "374764466575521",
        "SSN": "519-28-9198"
    },
    {
        "name": "Jessica Sawyer",
        "phone": "(547) 269-4650",
        "email": "dui@ipsumdolor.co.uk",
        "currency": "5824476662678552",
        "SSN": "479583578"
    },
    {
        "name": "Deborah Wilder",
        "phone": "(396) 526-5598",
        "email": "sodales.elit.erat@sed.com",
        "currency": "4903828368353837632",
        "SSN": "416159282"
    }
]

# source: https://www.amazon.com/dp/B00F4CFAV8/#customerReviews
reviews = [
    "Xbox game pass worked perfectly...Within a few minutes after checkout " +
    "I received the code. I used card number {currency}. Checkout my YouTube" +
    " channel or contact me {phone} or {email}. -{name}",

    "Hi I am {name}. I bought a card & it worked fine. About 2 weeks later " +
    "I ordered another but the code didn't work. Used same credit card " +
    "({currency}) and email ({email}). Please help ASAP! My cell {phone}.",

    "Until two weeks ago I would buy a card and get a code in minutes. Now " +
    "with my new credit card {currency} when I purchase a card it takes 24 " +
    "hours to get a code. I called Amazon & gave my details {name}; {email} " +
    "& {SSN}.",

    "I love the ease & quickness of purchasing the digital Xbox gift cards " +
    "instead of having to go to the store & waiting in line to buy a plastic" +
    " card that does the exact same thing as its digital counterpart. Save " +
    "yourself some time and gas. Just buy your gift cards here on Amazon and" +
    " get access to the funds instantly. The future is here people - take" +
    " advantage of it!",

    "Hey I am {name}. Email at {email} for free stuff. This is 100% legit " +
    "I bought these w my personal credit card {currency}. If you still " +
    "think I am a spammer - here is my social {SSN}!",

    "Intente comprar tarjetas digitales en Amazon. es una molestia usar mi " +
    "correo electronico {email} Simplemente compre las tarjetas prepagas en " +
    "la tienda"
]

with open(f"{f_name}.{f_ext}", "w") as file:
    file.write("id,raw_verbatim\n")
    for i, p in enumerate(people[:5]):
        idx = random.randint(0, len(reviews)-1)
        review = reviews[idx].format(name=p["name"], phone=p["phone"],
                                     email=p["email"], currency=p["currency"],
                                     SSN=p["SSN"])
        file.write(f"{i},{review}\n")
