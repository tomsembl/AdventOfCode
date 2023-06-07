def fizzbuzz():
    for x in range(31):
        output = ""
        if x % 3 == 0: output += "fizz"
        if x % 5 == 0: output += "buzz"
        if output=="":
            print(x)
        else: 
            print(output)
fizzbuzz()
#for x in range(31): print(x if (output:=("fizz" if x % 3 == 0 else "") + ("buzz" if x % 5 == 0 else ""))=="" else output)
public void uploadDocument(string filePath, string parentID, bool asNewVersion=false, string oldDocumentID="") { 
    
    string url = $"{urlPrefix}/api/v2/customers/{customerId}/libraries/{libraryName}/folders/{parentID}/documents";

    if (asNewVersion) { 
        url = $"{urlPrefix}/api/v2/customers/{customerId}/libraries/{libraryName}/documents/{oldDocumentID}/versions"; 
    }

    string fileName = System.IO.Path.GetFileName(filePath);
    string filenameWOExtension = System.IO.Path.GetFileNameWithoutExtension(filePath);
    string fileExtension = System.IO.Path.GetExtension(filePath).Substring(1);
    string boundary = $"----------{DateTime.Now.Ticks:x}";

    string profileJson = $"{{\"warnings_for_required_and_disabled_fields\":true,\"doc_profile\":{{\"name\":\"{filenameWOExtension}\",\"extension\":\"{fileExtension}\",\"author\":\"imanadmin\"}}}}";

    using (MultipartFormDataContent form = new(boundary)) {
    
        form.Headers.Remove("Content-Type");
        form.Headers.TryAddWithoutValidation("Content-Type", $"multipart/form-data; boundary={boundary}");

        form.Add(new StringContent(profileJson, Encoding.UTF8, "application/json"), "\"profile\"");
        form.Add(new StreamContent(System.IO.File.OpenRead(filePath)), "file", fileName);

        using (HttpClient client = new()) {
    
            client.DefaultRequestHeaders.Add("X-Auth-Token", getAccessToken().token);
            client.DefaultRequestHeaders.TransferEncodingChunked = false;
            string jsonString = "";

            async Task post() {
                var response = await client.PostAsync(url, form);
                jsonString = await response.Content.ReadAsStringAsync();
                Console.WriteLine(jsonString);
                response.EnsureSuccessStatusCode();
            }

            post().Wait();
        }
    }
}