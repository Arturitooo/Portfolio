
$(document).ready(function () {
    // Function to check and update password requirements indicators
    function checkPasswordRequirements() {
        var password = $('#id_password1').val();

        // Check each password requirement
        var isLengthValid = password.length >= 8;
        var hasUppercase = /[A-Z]/.test(password);
        var hasLowercase = /[a-z]/.test(password);
        var hasNumber = /\d/.test(password);
        var hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);

        // Update the indicators
        updateIndicator('length-indicator', isLengthValid, '8 characters');
        updateIndicator('uppercase-indicator', hasUppercase, 'one uppercase letter');
        updateIndicator('lowercase-indicator', hasLowercase, 'one lowercase letter');
        updateIndicator('number-indicator', hasNumber, 'one number');
        updateIndicator('special-char-indicator', hasSpecialChar, 'one special character')

        function updateIndicator(indicatorId, isValid) {
            var indicator = $('#' + indicatorId);

            // Update the text content
            indicator.text(isValid ? '✓' : '•');

            // Update the color
            indicator.css('color', isValid ? 'green' : 'rgba(237, 237, 237, 0.5)');
        }

        function updateIndicator(indicatorId, isValid, requirementText) {
            var indicator = $('#' + indicatorId);

            // Update the text content
            indicator.html(isValid ? '✓ ' + requirementText : '• ' + requirementText);

            // Update the color using CSS custom properties
            indicator.css('color', isValid ? 'green' : 'rgba(237, 237, 237, 0.5)');
        }

    }

    // Attach an event listener to the password input
    $('#id_password1').on('input', function () {
        checkPasswordRequirements();
    });
});
