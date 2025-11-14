import random

def list_attractions(date: str) -> dict:
    space_needle_times = randomize_business_time_slots()
    example_time = "9:00 AM"
    if example_time not in space_needle_times:
        space_needle_times.insert(0, example_time)
    attractions = {
        "Space Needle": {
            "times": space_needle_times,
            "price": "$74"
        },
        "Museum of Pop Culture": {
            "times": randomize_business_time_slots(),
            "price": "$10"
        },
        "Chihuly Glass Gardens": {
            "times": randomize_business_time_slots(),
            "price": "$34"
        }
    }
    return attractions

def randomize_business_time_slots():
    slots = [
        "9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM",
        "12:00 PM", "12:30 PM", "1:00 PM", "1:30 PM", "2:00 PM", "2:30 PM",
        "3:00 PM", "3:30 PM", "4:00 PM", "4:30 PM", "5:00 PM", "5:30 PM"
    ]
    num_slots = random.randint(2, 5)
    selected_slots = random.sample(slots, num_slots)
    return sorted(selected_slots, key=lambda x: slots.index(x))

def reserve_ticket(attraction: str, date: str, time: str) -> dict:
    reservation = {
        "reservationCode": generate_reservation_code()
    }
    return reservation

def generate_reservation_code():
    """Generate code with 2/3 chance of letters, 1/3 chance of numbers"""
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(chars) for _ in range(6))

def cancel_ticket(reservation_code: str) -> dict:
    reservation = {
        "status": "Success"
    }
    return reservation

def lambda_handler(event, context) -> dict:
    tool_name = context.client_context.custom['bedrockAgentCoreToolName']
    delimiter = "___"
    if delimiter in tool_name:
        tool_name = tool_name[tool_name.index(delimiter) + len(delimiter):]
    if tool_name == "list_attractions":
        response = list_attractions(event['date'])
    elif tool_name == "reserve_ticket":
        response = reserve_ticket(event['attraction'], event['date'], event['time'])
    elif tool_name == "cancel_ticket":
        response = cancel_ticket(event['reservationCode'])
    else:
        raise Exception("Unsupported tool")
    return response
