// Copyright (c) 2025, Daniot and contributors
// For license information, please see license.txt

frappe.ui.form.on("Loan", {
	validate: function (frm) {
		if (frm.doc.return_date <= frm.doc.loan_date) {
			frappe.throw("Return date must be after the loan date.");
		}
	},
});
