odoo.define('ap_password_manager.copy_decrypted_text_action', function (require) {
    "use strict";

    const AbstractAction = require('web.AbstractAction');
    const core = require('web.core');

    const CopyDecryptedTextAction = AbstractAction.extend({
        /**
         * Start the action and prevent any redirection.
         */
        start: function () {
            const self = this;

            // Prevent the default behavior when the button is clicked
            this.$el.on('click', function (event) {
                event.preventDefault();    // Prevent form submission or redirection
                event.stopPropagation();  // Stop the event from propagating further
            });

            return this._super.apply(this, arguments);
        },

        /**
         * Initialize the client action that handles the decrypted text.
         */
        init: function (parent, action) {
            this._super.apply(this, arguments);

            // Prevent default form submission or redirection again in case event is passed directly
            if (action && action.event) {
                action.event.preventDefault();
                action.event.stopPropagation();
            }

            const decryptedText = action.params.decrypted_text;

            // Create a temporary element to copy text to the clipboard
            const tempInput = document.createElement('textarea');
            tempInput.value = decryptedText;
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand('copy');
            document.body.removeChild(tempInput);

            // Notify the user that the text has been copied
            this.displayNotification({
                title: 'Success',
                message: 'Decrypted text copied to clipboard!',
                type: 'success',
                sticky: false,
            });
        }
    });

    core.action_registry.add('copy_decrypted_text', CopyDecryptedTextAction);  // Register the action

    return CopyDecryptedTextAction;
});