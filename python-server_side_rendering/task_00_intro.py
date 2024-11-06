import os


def generate_invitations(template, attendees):
    """
    Generate invitation letters for attendees based on the template.
    """

    try:
        if not isinstance(template, str):
            raise ValueError("Template must be a string")

        if not isinstance(attendees, list) or not \
                all(isinstance(item, dict) for item in attendees):
            raise ValueError("Attendees must be a list")

        if template.strip() == "":
            raise ValueError("Template is empty")

        if not attendees:
            raise ValueError("Attendees list is empty")

        if os.path.exists(file_name):
            print(f"File {file_name} already exists.")

        for attendee in attendees:
            if not all(key in attendee for key in \
                    ["name", "event_title", "event_date", "event_location"]):
                raise ValueError("Attendee must have keys")

        for index, attendee in enumerate(attendees, start=1):

            content = template.format(
                name=attendee.get("name", "N/A"),
                event_title=attendee.get("event_title", "N/A"),
                event_date=attendee.get("event_date", "N/A"),
                event_location=attendee.get("event_location", "N/A")
            )

            file_name = f"output_{index}.txt"
            with open(file_name, "w") as file:
                file.write(content)

            print(f"Invitation generated: {file_name}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
