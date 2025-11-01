# Define a function to display information about team members
def display_team_info(team_members):
    """
    Prints formatted information about each team member.
    
    Parameters:
        team_members (list): A list of dictionaries containing member details.
    """
    for member in team_members:
        print(
            f"Name: {member['name']}, "
            f"Username: {member['slack_username']}, "
            f"Country: {member['country']}, "
            f"Hobby: {member['hobby']}, "
            f"Affiliation: {member['affiliation']}, "
            f"Favourite gene: {member['fave_gene']}"
        )

# List of dictionaries containing team member information
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

# Call the function to print all members' info
display_team_info(team_tyrosine)
