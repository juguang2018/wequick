<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class White_black_list extends Model
{
    protected $table = 'white_black_lists';
    protected $fillable = ['cwxid','wxid', 'type','chatroom','nick','headPic','auth'];
}
