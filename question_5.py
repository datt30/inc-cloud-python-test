import json
import datetime

class TranscationDocumentHelper:

    TRANSACTION_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"
    DATE_FIELDS = [
        "claimDateTime",
        "fileDateTime",
        "receivedDateTime",
    ]

    def __init__(self, input_doc_path, output_doc_path):
        self.input_doc_path = input_doc_path
        self.output_doc_path = output_doc_path

        with open(self.input_doc_path, "r") as file:
          self.data = json.load(file)

    def _convert_timestamp_to_date_string(self, timestamp):
        datetime_obj = datetime.datetime.fromtimestamp(timestamp / 1e3)
        return datetime_obj.strftime(self.TRANSACTION_DATE_FORMAT)

    def get_payee_id(self):
      return self.data["payee"]["id"]

    def get_583_invoices(self):
      invoices = self.data["invoiceIds"]
      return [invoice_id for invoice_id in invoices if "583" in invoice_id]

    def update_date_fields_format(self):
      for field in self.DATE_FIELDS:
          if field in self.data:
              self.data[field] = self._convert_timestamp_to_date_string(self.data[field])

    def save_doc_changes(self):
      with open(self.output_doc_path, "w") as file:
          json.dump(self.data, file, indent=4)
      print(f"Updated JSON document written to {self.output_doc_path}")


transaction_document = TranscationDocumentHelper(
    input_doc_path="test_docs/input.json",
    output_doc_path="test_docs/output.json"
)
payee_id = transaction_document.get_payee_id()
print(f"Payee ID: {payee_id}")

matching_invoices = transaction_document.get_583_invoices()
print(f"Invoices containing '583': {matching_invoices}")

transaction_document.update_date_fields_format()
transaction_document.save_doc_changes()
