<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Friend extends Model
{
    protected $table = 'friends';
    protected $fillable = ['cwxid', 'wxid','nick', 'username','asName','headPic','sex','nationality', 'province','city', 'type','groupId'];
}
