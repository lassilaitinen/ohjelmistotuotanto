*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalleuusi  kalle321
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle321
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ke  kalle321
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kallö1  kalle321
    Output Should Contain  Username can't include numbers

Register With Valid Username And Too Short Password
    Input Credentials  kaalle  kk
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kkkkkkkkkkk
    Output Should Contain  Password cant include only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command 
