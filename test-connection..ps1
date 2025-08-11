
function Test-NetworkConnection {
    param (
        [int] $retry = 3
    )
    Test-Connection localhost -Count $retry
}

# Test-NetworkConnection -retry 4

# $users = @(
#     @{
#         id = 1;
#         name = "Demis";
#         age = 22;
#     },
#     @{
#         id = 2;
#         name = "Abel";
#         age = 23;
#     }
# );

# # foreach($user in $users){
# #     Write-Output  ("{ id: " + $user.id + ", name: " + $user.name + ", age: " + $user.age + " }")
# # }

# Function Receive-TCPMessage {
#  Param (
#  [Parameter(Mandatory=$true, Position=0)]
#  [ValidateNotNullOrEmpty()]
#  [int] $Port
#  )
#  Process {
#  Try {
#  # Set up endpoint and start listening
#  $endpoint = new-object System.Net.IPEndPoint([ipaddress]::any,$port)
#  $listener = new-object System.Net.Sockets.TcpListener $EndPoint
#  $listener.start()
#  # Wait for an incoming connection
#  $data = $listener.AcceptTcpClient()
 
#  # Stream setup
#  $stream = $data.GetStream()
#  $bytes = New-Object System.Byte[] 1024
#  # Read data from stream and write it to host
#  while (($i = $stream.Read($bytes,0,$bytes.Length)) -ne 0){
#  $EncodedText = New-Object System.Text.ASCIIEncoding
#  $data = $EncodedText.GetString($bytes,0, $i)
#  Write-Output $data
#  }
 
#  # Close TCP connection and stop listening
#  $stream.close()
#  $listener.stop()
#  }
#  Catch {
#  "Receive Message failed with: `n" + $Error[0]
#  }
#  }
# }

# # $msg = Receive-TCPMessage -Port 29800

# <#
# This 
# is multi line
# comment
# #>

# class Person {
#     [int] $id
#     [string] $name

#     Person([int] $id, [string] $name) {
#         $this.id = $id
#         $this.name = $name
#     }
#     [string] SayHello() {
#         return "Hello World"
#     }

#     [string] ToString() {
#         # return "{ id: {0} , name: {1} }" -f $this.id, $this.name
#         return ""
#     }
# }

# # $person = New-Object Person(1,"Demis")
# $person = [Person]::new(1,"Demis")

# Write-Output $person.SayHello()
# Write-Output $person.ToString()


# Get-Process | ForEach-Object -Process {
#     $PSItem.Name
# }

