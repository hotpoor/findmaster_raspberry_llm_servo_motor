root = exports ? this
root.Hs or= {}
Hs = root.Hs

$ ->
    console.log "index.coffee"


    $("body").on "click",".send_message",(evt)->
        workflow_id = "7508244556682281014"
        token = "pat_oVgsWHaa2P8kg3TDWPIN4XzAOJur4tXSFsK30n6TPnpst6GfQIDBpA6QGrdVtB4h"
        user_prompt = $(".current_message").val()
        data_need =
            "parameters":
                "user_prompt": user_prompt
                "chat_id": ""
                "messages_num": 0
            "workflow_id":workflow_id

        $(".messages").append """
            <div class="message">我：#{user_prompt}</div>
        """
        $(".current_message").val("")
        $.ajax
            url: 'https://api.coze.cn/v1/workflow/run'
            type: 'POST'
            headers:
                'Authorization': "Bearer #{token}"
                'Content-Type': 'application/json'
            data: JSON.stringify(data_need)
            success: (data)->
                console.log('Success:', data)
                output = JSON.parse(data.data)
                output_json = JSON.parse(output.output)
                console.log('output_json:', output_json)
                $(".messages").append """
                    <div class="message">AI：My feeling is #{output_json["feeling"]}.
                    </div>
                """
                actions_str = 
                    "servo_data":output_json["servo_data"]
                $.ajax
                    url: '/api/actions'
                    type: 'POST'
                    data: 
                        "actions_str":JSON.stringify(actions_str)
                    success:(data)->
                        console.log("data",data)
                    error:(error)->
                        console.log("error",error)
            error: (error)->
                console.error('Error:', error)