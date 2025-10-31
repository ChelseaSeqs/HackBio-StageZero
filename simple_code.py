team_tyrosine = [
    {
        "name": "Chelsea U",
        "slack_username": "Chels123",
        "country": "Germany",
        "hobby": "traveling",
        "affiliation": "Hackbio Intern",
        "fave_gene": "ATG"
    },
    {
        "name": "David O",
        "slack_username": "Dav123",
        "country": "Nigeria",
        "hobby": "cooking",
        "affiliation": "Hackbio Intern",
        "fave_gene": "TAG"
    },
    {
        "name": "Christopher A",
        "slack_username": "Chris123",
        "country": "Nigeria",
        "hobby": "football",
        "affiliation": "Hackbio Intern",
        "fave_gene": "TAA"
    }
]

for member in team_tyrosine:
    print(
        f"Name: {member['name']}, Username: {member['slack_username']}, Country: {member['country']}, "
        f"Hobby: {member['hobby']}, Affiliation: {member['affiliation']}, Favourite gene: {member['fave_gene']}"
    )
