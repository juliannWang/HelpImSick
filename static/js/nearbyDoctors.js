function getLocation() {
    console.log("this is working");
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
    }
    function showPosition(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    $.ajax({
        url: '',
        type: 'get',
        data: {
            'lat' : lat,
            'lon' : lon
        },
        success: function(response){
            console.log(response)
            $.each(response, function(index,response){
                var website = response.result.website;
                var rating = response.result.rating;
                var name = response.result.name;
                var phone_number = response.result.international_phone_number;
                var address = response.result.formatted_address;
                var opening_hours = response.result.opening_hours.weekday_text;


                var number_text = $('<h6>').text("Phone number:");
                var opening_hours_text = $('<h6>').text("Opening Hours:");
                var website_text = $('<h6>').text("Website:");
                var address_text = $('<h6>').text("Address:");

                var phone_number_element = $('<p>').text(phone_number);
                var website_element = $('<p>').text(website)
                var address_element = $('<p>').text(address)
                var name_element = $('<h2>').text(name);
                var opening_hours_element = $('<ul>');
                $.each(opening_hours, function(i, value) {
                    opening_hours_element.append($('<li>').text(value));
                });
                var rating_element = $('<p>').text('Rating: ' + rating);
                var elementID = '#' + index.toString();
                $(elementID).append(name_element);
                $(elementID).append(number_text);
                $(elementID).append(phone_number_element);
                $(elementID).append(opening_hours_text);
                $(elementID).append(opening_hours_element);
                $(elementID).append(rating_element);
                $(elementID).append(website_text);
                $(elementID).append(website_element);
                $(elementID).append(address_text);
                $(elementID).append(address_element);
            });
        }
    })
    }