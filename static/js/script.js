$(document).ready(function(){
    if($('#result') != null){
        Read();
    }
    $('#create').on('click', function(){
        $firstname = $('#firstname').val();
        $lastname = $('#lastname').val();

        if($firstname == "" || $lastname == ""){
            alert("Please complete the required field");
        }else{
            $.ajax({
                url: 'create',
                type: 'POST',
                data: {
                    firstname: $firstname,
                    lastname: $lastname,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    Read();
                    $('#firstname').val('');
                    $('#lastname').val('');
                }
            });
        }
    });

    $(document).on('click', '.edit', function(){
        $id = $(this).attr('name');
        window.location = "edit/" + $id;
    });

    $('#update').on('click', function(){
        $firstname = $('#firstname').val();
        $lastname = $('#lastname').val();

        if($firstname == "" || $lastname == ""){
            alert("Please complete the required field");
        }else{
            $id = $('#member_id').val();
            $.ajax({
                url: 'update/' + $id,
                type: 'POST',
                data: {
                    firstname: $firstname,
                    lastname: $lastname,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
              document.getElementById('res').innerHTML = "<div class='alert alert-success text-center'><span class='glyphicon glyphicon-info-sign'></span>تم تحديث البيانات !</div>";

                    setTimeout(function(){ window.location = '/crud'; }, 1500);;
                }
            });
        }

    });

    $(document).on('click', '.delete', function(){
        $id = $(this).attr('name');
        $.ajax({
            url: 'delete/' + $id,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
              document.getElementById('res').innerHTML = "<div class='alert alert-success text-center'><span class='glyphicon glyphicon-info-sign'></span>تمت عملية الحذف!</div>";
                Read();

            }
        });
    });

});

function Read(){
    $.ajax({
		url: 'read',
		type: 'POST',
		async: false,
		data:{
			res: 1,
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
		},
		success: function(response){
			$('#result').html(response);
		}
    });
}