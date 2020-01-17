<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Zombie extends Model
{
    protected $table = 'zombies';
    protected $fillable = ['cwxid', 'wxid','nick', 'username','asName','headPic','sex'];
}
