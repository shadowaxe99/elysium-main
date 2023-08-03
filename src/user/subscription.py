```python
import stripe
from .account import User

stripe.api_key = "your_stripe_api_key"

class Subscription:
    def __init__(self, user: User):
        self.user = user

    def create_subscription(self, plan_id: str):
        try:
            subscription = stripe.Subscription.create(
                customer=self.user.stripe_customer_id,
                items=[
                    {"plan": plan_id},
                ],
            )
            self.user.subscription_id = subscription.id
            return subscription
        except Exception as e:
            print(f"Failed to create subscription: {e}")
            return None

    def cancel_subscription(self):
        try:
            subscription = stripe.Subscription.retrieve(self.user.subscription_id)
            subscription.delete()
            self.user.subscription_id = None
            return True
        except Exception as e:
            print(f"Failed to cancel subscription: {e}")
            return False

    def update_subscription(self, new_plan_id: str):
        try:
            subscription = stripe.Subscription.retrieve(self.user.subscription_id)
            subscription.items = [
                {"plan": new_plan_id},
            ]
            subscription.save()
            return subscription
        except Exception as e:
            print(f"Failed to update subscription: {e}")
            return None
```