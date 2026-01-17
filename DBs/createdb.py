import sqlite3

def create_booker_db():
    conn = sqlite3.connect('booker_prize.db')
    cursor = conn.cursor()

    # Create the table with new columns for rating and votes
    cursor.execute('DROP TABLE IF EXISTS nominations')
    cursor.execute('''
        CREATE TABLE nominations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER,
            author TEXT,
            title TEXT,
            status TEXT DEFAULT 'Longlist',
            rating REAL,
            votes INTEGER
        )
    ''')

    # Data Format: (Year, Author, Title, Status, Rating, Votes)
    # Note: Ratings/Votes are based on approximate Goodreads data at the time of retrieval.
    data = [
        # --- 2025 (Winner/Shortlist announced Nov 2025) ---
        (2025, "David Szalay", "Flesh", "Winner", None, None),
        (2025, "Susan Choi", "Flashlight", "Shortlist", None, None),
        (2025, "Kiran Desai", "The Loneliness of Sonia and Sunny", "Shortlist", None, None),
        (2025, "Katie Kitamura", "Audition", "Shortlist", None, None),
        (2025, "Ben Markovits", "The Rest of Our Lives", "Shortlist", None, None),
        (2025, "Andrew Miller", "The Land in Winter", "Shortlist", None, None),
        (2025, "Claire Adam", "Love Forms", "Longlist", None, None),
        (2025, "Tash Aw", "The South", "Longlist", None, None),
        (2025, "Natasha Brown", "Universality", "Longlist", None, None),
        (2025, "Jonathan Buckley", "One Boat", "Longlist", None, None),
        (2025, "Maria Reva", "Endling", "Longlist", None, None),
        (2025, "Benjamin Wood", "Seascraper", "Longlist", None, None),
        (2025, "Ledia Xhoga", "Misinterpretation", "Longlist", None, None),

        # --- 2024 ---
        (2024, "Samantha Harvey", "Orbital", "Winner", 3.51, 133595),
        (2024, "Percival Everett", "James", "Shortlist", 4.44, 470354),
        (2024, "Rachel Kushner", "Creation Lake", "Shortlist", 3.35, 33772),
        (2024, "Anne Michaels", "Held", "Shortlist", 3.50, 11303),
        (2024, "Yael van der Wouden", "The Safekeep", "Shortlist", 4.08, 86983),
        (2024, "Charlotte Wood", "Stone Yard Devotional", "Shortlist", 3.74, 23585),
        (2024, "Colin Barrett", "Wild Houses", "Longlist", 3.70, 8314),
        (2024, "Rita Bullwinkel", "Headshot", "Longlist", 3.48, 14056),
        (2024, "Hisham Matar", "My Friends", "Longlist", 4.28, 14291),
        (2024, "Claire Messud", "This Strange Eventful History", "Longlist", 3.56, 5566),
        (2024, "Tommy Orange", "Wandering Stars", "Longlist", 3.82, 36590),
        (2024, "Sarah Perry", "Enlightenment", "Longlist", 3.57, 5028),
        (2024, "Richard Powers", "Playground", "Longlist", 4.15, 40928),

        # --- 2023 ---
        (2023, "Paul Lynch", "Prophet Song", "Winner", 4.03, 83401),
        (2023, "Sarah Bernstein", "Study for Obedience", "Shortlist", 3.01, 13563),
        (2023, "Jonathan Escoffery", "If I Survive You", "Shortlist", 3.68, 13358),
        (2023, "Paul Harding", "This Other Eden", "Shortlist", 3.76, 21338),
        (2023, "Chetna Maroo", "Western Lane", "Shortlist", 3.48, 10819),
        (2023, "Paul Murray", "The Bee Sting", "Shortlist", 3.88, 132035),
        (2023, "Ayọ̀bámi Adébáyọ̀", "A Spell of Good Things", "Longlist", 3.78, 6997),
        (2023, "Sebastian Barry", "Old God's Time", "Longlist", 3.80, 18781),
        (2023, "Tan Twan Eng", "The House of Doors", "Longlist", 4.10, 22782),
        (2023, "Elaine Feeney", "How to Build a Boat", "Longlist", 3.73, 6571),
        (2023, "Siân Hughes", "Pearl", "Longlist", 3.85, 6312),
        (2023, "Viktoria Lloyd-Barlow", "All the Little Bird-Hearts", "Longlist", 3.76, 5286),
        (2023, "Martin MacInnes", "In Ascension", "Longlist", 3.74, 14953),

        # --- 2022 ---
        (2022, "Shehan Karunatilaka", "The Seven Moons of Maali Almeida", "Winner", 3.90, 59832),
        (2022, "NoViolet Bulawayo", "Glory", "Shortlist", 3.70, 5817),
        (2022, "Percival Everett", "The Trees", "Shortlist", 4.06, 55727),
        (2022, "Alan Garner", "Treacle Walker", "Shortlist", 3.35, 10717),
        (2022, "Claire Keegan", "Small Things Like These", "Shortlist", 4.09, 433821),
        (2022, "Elizabeth Strout", "Oh William!", "Shortlist", 3.86, 94184),
        (2022, "Graeme Macrae Burnet", "Case Study", "Longlist", 3.57, 11928),
        (2022, "Hernan Diaz", "Trust", "Longlist", 3.80, 172382),
        (2022, "Karen Joy Fowler", "Booth", "Longlist", 3.83, 15138),
        (2022, "Audrey Magee", "The Colony", "Longlist", 4.11, 12657),
        (2022, "Maddie Mortimer", "Maps of Our Spectacular Bodies", "Longlist", 3.96, 7237),
        (2022, "Leila Mottley", "Nightcrawling", "Longlist", 3.95, 60090),
        (2022, "Selby Wynn Schwartz", "After Sappho", "Longlist", 3.51, 5243),

        # --- 2021 ---
        (2021, "Damon Galgut", "The Promise", "Winner", 3.85, 49419),
        (2021, "Anuk Arudpragasam", "A Passage North", "Shortlist", 3.70, 8874),
        (2021, "Patricia Lockwood", "No One Is Talking About This", "Shortlist", 3.55, 54874),
        (2021, "Nadifa Mohamed", "The Fortune Men", "Shortlist", 3.79, 5644),
        (2021, "Richard Powers", "Bewilderment", "Shortlist", 3.91, 70602),
        (2021, "Maggie Shipstead", "Great Circle", "Shortlist", 4.09, 81041),
        (2021, "Rachel Cusk", "Second Place", "Longlist", 3.67, 27840),
        (2021, "Nathan Harris", "The Sweetness of Water", "Longlist", 4.25, 140000), # Approx
        (2021, "Kazuo Ishiguro", "Klara and the Sun", "Longlist", 3.74, 428038),
        (2021, "Karen Jennings", "An Island", "Longlist", 3.54, 4109),
        (2021, "Mary Lawson", "A Town Called Solace", "Longlist", 4.01, 28878),
        (2021, "Sunjeev Sahota", "China Room", "Longlist", 3.77, 10539),
        (2021, "Francis Spufford", "Light Perpetual", "Longlist", None, None),

        # --- 2020 ---
        (2020, "Douglas Stuart", "Shuggie Bain", "Winner", 4.30, 189067),
        (2020, "Diane Cook", "The New Wilderness", "Shortlist", 3.67, 16440),
        (2020, "Tsitsi Dangarembga", "This Mournable Body", "Shortlist", 3.33, 4940),
        (2020, "Avni Doshi", "Burnt Sugar", "Shortlist", 3.25, 26010),
        (2020, "Maaza Mengiste", "The Shadow King", "Shortlist", 3.65, 14888),
        (2020, "Brandon Taylor", "Real Life", "Shortlist", 3.78, 37141),
        (2020, "Gabriel Krauze", "Who They Was", "Longlist", 4.02, 4790),
        (2020, "Hilary Mantel", "The Mirror & the Light", "Longlist", 4.40, 46539),
        (2020, "Colum McCann", "Apeirogon", "Longlist", 4.25, 26708),
        (2020, "Kiley Reid", "Such a Fun Age", "Longlist", 3.77, 573881),
        (2020, "Anne Tyler", "Redhead by the Side of the Road", "Longlist", 3.61, 50910),
        (2020, "Sophie Ward", "Love and Other Thought Experiments", "Longlist", 3.59, 6126),
        (2020, "C Pam Zhang", "How Much of These Hills Is Gold", "Longlist", 3.78, 26377),

        # --- 2019 ---
        (2019, "Margaret Atwood", "The Testaments", "Winner", 4.20, 421605),
        (2019, "Bernardine Evaristo", "Girl, Woman, Other", "Winner", 4.26, 263837),
        (2019, "Salman Rushdie", "Quichotte", "Shortlist", 3.81, 10632),
        (2019, "Lucy Ellmann", "Ducks, Newburyport", "Shortlist", 3.97, 5844),
        (2019, "Chigozie Obioma", "An Orchestra of Minorities", "Shortlist", 3.69, 6281),
        (2019, "Elif Shafak", "10 Minutes 38 Seconds...", "Shortlist", 4.09, 83155),
        (2019, "Kevin Barry", "Night Boat to Tangier", "Longlist", 3.62, 21813),
        (2019, "Oyinkan Braithwaite", "My Sister, The Serial Killer", "Longlist", 3.64, 351331),
        (2019, "John Lanchester", "The Wall", "Longlist", 3.60, 11000),
        (2019, "Deborah Levy", "The Man Who Saw Everything", "Longlist", 3.67, 11517),
        (2019, "Valeria Luiselli", "Lost Children Archive", "Longlist", 3.80, 25406),
        (2019, "Max Porter", "Lanny", "Longlist", 4.05, 30413),
        (2019, "Jeanette Winterson", "Frankissstein", "Longlist", 3.53, 14253),
    ]

    cursor.executemany('''
        INSERT INTO nominations (year, author, title, status, rating, votes) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', data)
    
    conn.commit()
    print(f"Database 'booker_prize.db' created with ratings and votes for {len(data)} books.")
    
    # Verify: Print top 5 highest rated books
    print("\nTop 5 Highest Rated Books:")
    cursor.execute("SELECT title, author, rating FROM nominations WHERE rating IS NOT NULL ORDER BY rating DESC LIMIT 5")
    for row in cursor.fetchall():
        print(f"{row[0]} by {row[1]} - {row[2]}")

    conn.close()

if __name__ == "__main__":
    create_booker_db()