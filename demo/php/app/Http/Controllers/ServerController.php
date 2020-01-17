<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ServerController extends Controller
{
  protected $cnt = 1;
  public function recieve(Request $request)
  {
    $request_object = $request->get('data');
    
    $path = public_path();
    $file = $path."\\recieve.log";
    $myfile = fopen($file, "a") or die("Unable to open file!");
    fwrite($myfile, json_encode($request_object)."\r\n\r\n");
    fclose($myfile);

    return  json_encode($request_object);
  }
  public function send()
  {
    $res = [];
    if($this->cnt == 1){
      $send_dict = [];
      // $send_dict = [
      //   "api"=>"sendTextMessage",
      //   "sendId"=>"8859663",
      //   "option"=>[
      //     "wxid"=>"xyz103053",
      //     "text"=>"星星555"
      //   ]
      // ];
      array_push($res,$send_dict);
      $this->cnt += 1;
    }
    $this->cnt = 0;
    return json_encode($res);
  }
}
