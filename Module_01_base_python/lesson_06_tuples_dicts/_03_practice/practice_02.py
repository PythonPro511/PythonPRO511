# projects = {}
# projects[(101, "Project Alpha")] = {"participants": {"Alice": "Lead", "Bob": "Developer"}}
# projects[(102, "Project Beta")] = {"participants": {"Charlie": "Manager", "Dave": "Analyst"}}

projects = {
    (101, "Project Alpha"): {"participants": {"Alice": "Lead", "Bob": "Developer"}},
    (102, "Project Beta"): {"participants": {"Charlie": "Manager", "Dave": "Analyst"}}
}

for (proj_id, title), details in projects.items():
    print(f'Проект {proj_id}: {title}')
    for name, role in details['participants'].items():
        print(f'{name} - {role}')
    print()
