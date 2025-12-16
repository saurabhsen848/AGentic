Initial project code upload
tasks = [
    {
        "name": "Learn Python Basics",
        "duration": 2,
        "priority": 1,
        "dependencies": []
    },
    {
        "name": "Learn OOP Concepts",
        "duration": 3,
        "priority": 2,
        "dependencies": ["Learn Python Basics"]
    },
    {
        "name": "Learn DBMS",
        "duration": 2,
        "priority": 2,
        "dependencies": []
    },
    {
        "name": "Learn Machine Learning",
        "duration": 4,
        "priority": 3,
        "dependencies": ["Learn OOP Concepts"]
    }
]
