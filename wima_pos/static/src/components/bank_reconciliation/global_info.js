/** @odoo-module **/
import { Component } from "@odoo/owl";

export class BankRecGlobalInfo extends Component {
    static template = "wima_pos.BankRecGlobalInfo";
    static props = {
        journalId: { type: Number },
        journalBalanceAmount: { type: String },
    };

    /** Open the bank reconciliation report. **/
    actionOpenBankGL() {
        this.env.methods.actionOpenBankGL(this.props.journalId);
    }

}
