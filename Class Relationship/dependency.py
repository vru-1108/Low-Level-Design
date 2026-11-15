class SeatValidator:
    def is_available(self, event_id, seat_number):
        print(f"Checking seat {seat_number} for event {event_id}")
        return True  # Simulated: seat is available

class PaymentProcessor:
    def charge(self, email, amount):
        print(f"Charging ${amount} to {email}")
        return True  # Simulated: payment succeeds

class QRCodeGenerator:
    def generate(self, event_id, seat_number):
        qr_code = f"QR-{event_id}-{seat_number}"
        print(f"Generated QR code: {qr_code}")
        return qr_code

class EmailService:
    def send_confirmation(self, email, qr_code):
        print(f"Sending confirmation to {email} with code {qr_code}")

class TicketBookingService:
    def book_ticket(self, event_id, seat_number, email, amount,
                    validator, payment, qr_generator, email_service):
        if not validator.is_available(event_id, seat_number):
            print("Seat not available.")
            return False

        if not payment.charge(email, amount):
            print("Payment failed.")
            return False

        qr_code = qr_generator.generate(event_id, seat_number)
        email_service.send_confirmation(email, qr_code)

        print("Booking confirmed!")
        return True
		
if __name__ == "__main__":
    booking_service = TicketBookingService()

    # All dependencies are created externally and passed in
    validator = SeatValidator()
    payment = PaymentProcessor()
    qr_generator = QRCodeGenerator()
    email_service = EmailService()

    booking_service.book_ticket("CONF-2025", "A12", "alice@example.com",
        99.99, validator, payment, qr_generator, email_service)		