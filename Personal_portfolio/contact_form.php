<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Google Fonts: -->
    <link href="https://fonts.googleapis.com/css2?family=Kalam:wght@300;400;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Rock+Salt&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" href="includes/css/style.css">
    <link rel="icon" href="includes/images/logo.ico">
    <title>Contact me</title>
</head>
<body>
    <section>
        <h1>Thank you for contacting me, i will reply as soon as possible.</h1>    
        <?php
            $email_to = "krenyh313@gmail.com";
            $email_subject = "New form submissions";
            $email_message = "Form details below.\n\n";

            $name = $_GET["name"];
            $email = $_GET["email"];
            $subject = $_GET["subject"];
            $message = $_GET["message"];

            $email_message .= "Name: " . clean_string($name) . "\n";
            $email_message .= "Email: " . clean_string($email) . "\n";
            $email_message .= "Message: " . clean_string($message) . "\n";
           
            $headers = 'From: ' . $email . "\r\n" .
            'Reply-To: ' . $email . "\r\n" .
            'X-Mailer: PHP/' . phpversion();
            @mail($email_to, $email_subject, $email_message, $headers);
        ?> 
        <a href="index.html">go back</a>       
    </section>
</body>
</html>