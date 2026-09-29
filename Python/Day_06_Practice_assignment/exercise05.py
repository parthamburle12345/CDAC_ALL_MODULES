class Notifier:
    def __init__(self, sender_id, **kwargs):
        super().__init__(**kwargs)
        self.sender_id = sender_id

    def send(self, message):
        return [f"[Notifier {self.sender_id}] general broadcast: {message}"]


class EmailNotifier(Notifier):
    def __init__(self, email_server, **kwargs):
        self.email_server = email_server
        super().__init__(**kwargs)

    def send(self, message):
        logs = super().send(message)
        return [f"[Email via {self.email_server}] sending: {message}"] + logs


class SMSNotifier(Notifier):
    def __init__(self, sms_gateway, **kwargs):
        self.sms_gateway = sms_gateway
        super().__init__(**kwargs)

    def send(self, message):
        logs = super().send(message)
        return [f"[SMS via {self.sms_gateway}] sending: {message}"] + logs


class HybridAlertChannel(EmailNotifier, SMSNotifier):
    def __init__(self, sender_id, email_server, sms_gateway, **kwargs):
        # Cooperatively initialize via super() down the MRO
        super().__init__(
            sender_id=sender_id,
            email_server=email_server,
            sms_gateway=sms_gateway,
            **kwargs
        )

    def send(self, message):
        logs = super().send(message)
        return ["[HYBRID ALERT] Initiating dual channels..."] + logs


# Example Walkthrough
if __name__ == "__main__":
    # Print MRO to verify cooperative resolution path
    print("Method Resolution Order (MRO):", [cls.__name__ for cls in HybridAlertChannel.mro()])
    print()

    alert = HybridAlertChannel(sender_id="SYS-ADMIN", email_server="smtp.cdac.in", sms_gateway="gw.acts.com")
    logs = alert.send("Disk space 95%")

    for log in logs:
        print(log)
