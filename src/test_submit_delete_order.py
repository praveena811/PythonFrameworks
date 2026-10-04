import requests
import json


BASE_URL = "https://simple-books-api.glitch.me"  # Replace with your actual API base URL
Auth_Token = "25e04ae203049ddf9c13b83ea9130ca3e0b26f66a2e046bebafa7a8852bf5fab"

def test_submit_delete_order():
        # Step 1: Submit an order
        submit_order_url = f"{BASE_URL}/orders"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {Auth_Token}"
        }
        order_data = {
            "bookId": 1,  # Replace with a valid book ID
            "customerName": "John Doe"
        }
        response = requests.post(submit_order_url, headers=headers, data=json.dumps(order_data))
        assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
        
        # Extract the order ID from the response
        order_id = response.json().get("orderId")
        assert order_id is not None, "Order ID not found in the response"

        # Step 2: Delete the submitted order
        delete_order_url = f"{BASE_URL}/orders/{order_id}"
        delete_response = requests.delete(delete_order_url, headers=headers)
        assert delete_response.status_code == 204, f"Expected status code 204, but got {delete_response.status_code}"
        print(f"Order with ID {order_id} has been successfully deleted.")

if __name__ == "__main__":
    test_submit_delete_order()


